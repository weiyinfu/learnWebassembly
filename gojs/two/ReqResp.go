package main

import (
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"reflect"
)

type HandleFunction func(interface{}) interface{}
type Handler struct {
	HandleFunction HandleFunction
	RequestType    interface{}
}

func Handle(v Handler, requestString string) (string, error) {
	req := reflect.New(reflect.TypeOf(v.RequestType))
	err := json.Unmarshal(([]byte)(requestString), &req)
	if err != nil {
		fmt.Printf("解析请求错误%v", err)
		return "", err
	}
	resp := v.HandleFunction(req)
	respString, err := json.Marshal(resp)
	if err != nil {
		fmt.Printf("序列化Response错误%v", err)
		return "", err
	}
	return string(respString), nil
}

type TwoEatOneSolveRequest struct {
	NodeString string
	Who        int
}
type MammalSolveRequest struct {
	Board   []int
	Unknown []int
	Who     int
}

type HelloRequest struct {
}

func Get() map[string]Handler {
	return map[string]Handler{
		"TwoEatOneSolve": {
			HandleFunction: func(req interface{}) interface{} {
				return gin.H{}
			},
			RequestType: &TwoEatOneSolveRequest{},
		},
		"MammalSolve": {
			HandleFunction: func(req interface{}) interface{} {
				return gin.H{}
			},
			RequestType: &MammalSolveRequest{},
		},
		"hello": {
			HandleFunction: func(i interface{}) interface{} {
				return gin.H{
					"data": "hello world",
				}
			},
			RequestType: &HelloRequest{},
		},
	}
}
