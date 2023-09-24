package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/hex"
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

var aesKey []byte

func main() {
	router := gin.Default()

	// 生成AES密钥
	aesKey = generateAESKey()

	// 显示随机生成的16字节ID的加密结果以及输入框
	router.GET("/", func(c *gin.Context) {
		randomID := generateRandomID()
		encryptedID := encrypt(randomID, aesKey)
		c.HTML(http.StatusOK, "index.html", gin.H{
			"Token": hex.EncodeToString(encryptedID),
		})
	})

	// 处理用户输入的token并解密
	router.POST("/check", func(c *gin.Context) {
		tokenHex := c.PostForm("token")
		token, err := hex.DecodeString(strings.TrimSpace(tokenHex))
		if err != nil {
			c.String(http.StatusBadRequest, "Invalid token")
			return
		}

		decryptedToken := decrypt(token, aesKey)

		if len(decryptedToken) == 1 {
			http.Redirect(c.Writer, c.Request, "/1.php", http.StatusSeeOther)
		} else {
			c.String(http.StatusOK, "Token decrypted: %s\n", decryptedToken)
		}
	})

	router.Static("/assets", "./assets")
	router.LoadHTMLGlob("templates/*.html")

	router.Run(":23333")
}

func generateRandomID() []byte {
	randomID := make([]byte, 16)
	_, err := rand.Read(randomID)
	if err != nil {
		panic(err)
	}
	return randomID
}

func generateAESKey() []byte {
	aesKey := make([]byte, 32) // AES-256
	_, err := rand.Read(aesKey)
	if err != nil {
		panic(err)
	}
	return aesKey
}

func encrypt(data []byte, key []byte) []byte {
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	ciphertext := make([]byte, aes.BlockSize+len(data))
	iv := ciphertext[:aes.BlockSize]
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		panic(err)
	}

	mode := cipher.NewCBCEncrypter(block, iv)
	mode.CryptBlocks(ciphertext[aes.BlockSize:], data)

	return ciphertext
}

func decrypt(data []byte, key []byte) []byte {
	block, err := aes.NewCipher(key)
	if err != nil {
		panic(err)
	}

	if len(data) < aes.BlockSize {
		panic("Ciphertext too short")
	}

	iv := data[:aes.BlockSize]
	data = data[aes.BlockSize:]

	mode := cipher.NewCBCDecrypter(block, iv)
	mode.CryptBlocks(data, data)

	return data
}
