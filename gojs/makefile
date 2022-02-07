.PHONY:
	echo "haha"
prepare:
	python prepare.py
one:.PHONY
	GOARCH=wasm GOOS=js go build -o dist/one.wasm one/main.go
ls:
	ls -lh dist/