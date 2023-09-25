package main

import (
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "encoding/hex"
    "net/http"
    "bytes"
    "fmt"
    "github.com/gin-gonic/gin"
)

var key []byte
var iv []byte

func main() {
    fmt.Println("hello world!")
    key = generateRandomBytes(16)
    iv = generateRandomBytes(16)
    fmt.Println(key)
    fmt.Println(iv)

    router := gin.Default()
    router.LoadHTMLGlob("templates/*")

    router.StaticFile("/accept.php", "./accept.php")
    router.StaticFile("/unaccept.php", "./unaccept.php")

    router.GET("/", func(c *gin.Context) {
        sessionID := generateRandomBytes(16)
        token, err := encryptAES(sessionID, key, iv)
        if err != nil {
            c.String(http.StatusInternalServerError, "Error encrypting sessionID")
            return
        }

        c.SetSameSite(http.SameSiteStrictMode)
        c.SetCookie("sessionToken", hex.EncodeToString(token), 0, "/", "", true, true)

        c.HTML(http.StatusOK, "index.html", nil)
    })

    router.POST("/decrypt", func(c *gin.Context) {
        inputHex := c.PostForm("inputHex")
        inputBytes, err := hex.DecodeString(inputHex)
        if err != nil {
            c.Redirect(http.StatusSeeOther, "/unaccept.php")
            return
        }

        decrypted, err := decryptAES(inputBytes, key, iv)
        if err != nil || len(decrypted) != 1 {
            
            c.Redirect(http.StatusSeeOther, "/unaccept.php")
            return
        }

        c.Redirect(http.StatusSeeOther, "/accept.php")
    })

    router.Run(":8080")
}

func generateRandomBytes(length int) []byte {
    bytes := make([]byte, length)
    _, err := rand.Read(bytes)
    if err != nil {
        panic(err)
    }
    return bytes
}

func encryptAES(data []byte, key []byte, iv []byte) ([]byte, error) {
    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    paddedData := pkcs7Pad(data)
    ciphertext := make([]byte, len(paddedData))

    mode := cipher.NewCBCEncrypter(block, iv)
    mode.CryptBlocks(ciphertext, paddedData)

    return ciphertext, nil
}

func decryptAES(data []byte, key []byte, iv []byte) ([]byte, error) {
    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    mode := cipher.NewCBCDecrypter(block, iv)
    decryptedData := make([]byte, len(data))
    mode.CryptBlocks(decryptedData, data)

    return pkcs7Unpad(decryptedData), nil
}

func pkcs7Pad(data []byte) []byte {
    padSize := aes.BlockSize - (len(data) % aes.BlockSize)
    padding := bytes.Repeat([]byte{byte(padSize)}, padSize)
    fmt.Println("padded data:")
    fmt.Println(append(data, padding...))
    return append(data, padding...)
}

func pkcs7Unpad(data []byte) []byte {
    padSize := int(data[len(data)-1])
    fmt.Println("unpadded data:") 
    fmt.Println(data[:len(data)-padSize])
    return data[:len(data)-padSize]
}
