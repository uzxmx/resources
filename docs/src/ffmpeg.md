# FFmpeg

```
/usr/local/bin/ffmpeg -rtsp_transport tcp -i rtsp://admin:123456@192.168.1.102:
554/12 -vcodec copy -acodec copy  -t 10 -fs 10485760 -movflags faststart -y testa.mp4

/usr/local/bin/ffmpeg -rtsp_transport tcp -i rtsp://admin:123456@192.168.1.102:
554/12 -vcodec copy -acodec aac  -t 10 -fs 10485760 -movflags faststart -y testa.mp4

-acodec 指定输出文件的编码格式

mp4格式的音频不支持 adpcm_g726格式的编码
```

```
https://github.com/wez/atomicparsley/blob/master/src/main.cpp

AtomicParsley input.mp4 -T
```


ffmpeg -f avfoundation  -i 1 output.mkv

ffmpeg -ss 30 -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

ffmpeg -i output.mkv -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

ffmpeg -i output.mkv -vf "fps=10,scale=1024:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output1.gif

ffmpeg -i output.mkv -vf "fps=10,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

ffplay -i output.mkv -vf "crop=in_w:in_h-100"

ffplay -ss 2 -i output1.mkv -vf "crop=2450:1475:465:220,scale=1200:-1"

ffplay -ss 2 -i output1.mkv -vf "crop=2450:1475:465:220"

ffplay -i output.mkv -vf "crop=2440:1475:465:220" -ss 00:01:11

ffplay -i output.mkv -vf "select=between(n\,120\,2100),crop=2440:1475:465:220"
ffplay -i output.mkv -vf "select=gte(n\, 120),crop=2440:1475:465:220"

ffmpeg -i output.mkv -vf "select=between(n\,120\,2100),crop=2434:1468:465:220" -loop 0 output.gif
