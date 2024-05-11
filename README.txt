1 下载一张图片
2 在postman进行SAM解析，结果保存为xxx.txt
3 启动label，执行python converte.py From.txt To.json width height
4 生成的结果手动处理：1 外层括号 2 文件路径 3 在label系统建立对应的新tag 4 导入label

1 内部id唯一 DONE
2 内部坐标*100 DONE
3 外部文件路径
4 外部数组括号[]
5 标签大小写 DONE

已支持
单图多标签

TODO
多文件处理