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



func GenerateKey() []byte {
	key := make([]byte, 32) 
	_, err := rand.Read(key) 
	if err != nil {
		panic(err) 
	}
	return key 
}

func GenerateId() []byte {
	id := make([]byte, 20) 
	_, err := rand.Read(id) 
	if err != nil {
		panic(err) 
	}
	return id 
}

func padding(data []byte, blockSize int) []byte { 

    paddlen := blockSize - (len(data) % blockSize)
    pad := bytes.Repeat([]byte{byte(paddlen)}, paddlen) 
    return append(data, pad...)
}

func unpadding(data []byte) []byte {
	padlen := int(data[len(data)-1]) 
	return data[:len(data)-padlen]
}

func encrypt(pt []byte, key []byte) []byte {
	data := padding(pt) 
	block, err := aes.NewCipher(key) 
	if err != nil {
		panic(err)
	}

	ct := make([]byte, aes.BlockSize+)
}

var key []byte 

func main() {
	router := gin.Default() 
}