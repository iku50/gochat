package logic

import (
	"github.com/DataDog/go-python3"
)

func init() {
	python3.Py_Initialize()
	if !python3.Py_IsInitialized() {
		fmt.Println("Error initializing the python interpreter")
		os.Exit(1)
	}
}

func ImportModule(dir, name string) *python3.PyObject {
   sysModule := python3.PyImport_ImportModule("sys") 
   path := sysModule.GetAttrString("path")                    
   python3.PyList_Insert(path, 0, python3.PyUnicode_FromString("~/.conda/envs/chatemoji/lib/python3.9/site-packages"))
   python3.PyList_Insert(path, 0, python3.PyUnicode_FromString(dir)
   return python3.PyImport_ImportModule(name)           
}

func StringToEmojiNumber(str string) (emojiNumber int) {
	//TODO
	//调用python脚本
	//返回emojiNumber
	pyScript := ImportModule("../sentiment_classify","test")
	
	return
}
