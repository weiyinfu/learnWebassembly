package main

import (
	"fmt"
	"syscall/js"
	"time"
)

func main() {
	// 将golang中foo函数注入到window.foo中
	g := js.Global()
	g.Set("foo", js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		fmt.Println("hello")
		return "hello"
	}))
	// 将100注入到 window.value中
	g.Set("getTime", js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		return time.Now().String()
	}))
	g.Set("setText", js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		// 获取DOM元素, 进行设置属性,  call方法为调用js方法
		g.Get("document").Call("querySelector", "body").Set("innerHTML", args[0].String())
		return nil
	}))
	g.Set("sum", js.FuncOf(func(this js.Value, args []js.Value) interface{} {
		s := 0.
		for _, i := range args {
			fmt.Println(i)
			s += i.Float()
		}
		return s
	}))
	g.Set("value", 100)
	select {}
}
