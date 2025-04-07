#!/bin/bash

input_folder="jpgs"
output_folder="pngs"

mkdir -p "$output_folder"

for img in "$input_folder"/*.jpg; do
	filename=$(basename "$img" .jpg)
	convert "$img" -resize 800x600 "$output_folder/$filename.png"
done

echo "Image resizing and conversion done."

