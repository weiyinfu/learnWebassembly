package main

import (
	"fmt"
	"runtime"
	"syscall/js"
)

/**
使用Req和Response封装结构体的方式来简化js和go之间的通信
*/
func Register(ma map[string]Handler) {
	g := js.Global()
	for k, v := range ma {
		g.Set(k, js.FuncOf(func(this js.Value, args []js.Value) interface{} {
			s := args[0].String()
			respString, err := Handle(v, s)
			if err != nil {
				fmt.Println(err)
			}
			return respString
		}))
	}
	defer func() {
		// 发生宕机时，获取panic传递的上下文并打印
		err := recover()
		switch err.(type) {
		case runtime.Error: // 运行时错误
			fmt.Println("runtime error:", err)
		default: // 非运行时错误
			fmt.Println("error:", err)
		}
	}()
	select {}
}

func main() {
	Register(Get())
}
