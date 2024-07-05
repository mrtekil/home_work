#!/bin/bash

# Путь до директории с файлами
DIR=/tmp/attachments

# Счетчик скачиваний
count=20

# Проверка, что директория не существует и если истина, то создаем ее.
if [ ! -d $DIR ]; then
	mkdir $DIR
fi

# Обращаемся в цикле к ресурсу для загрузки изображений
for ((i = 1; i <= count; i++))
do
	echo download file number $i
	curl https://picsum.photos/800/400 -L > $DIR/$i.jpg
done

