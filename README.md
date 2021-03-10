# News-img-Spider

## Discription
A very very easy spider based on Scrapy.&emsp;
(Of course, the whole process has a key point that has been described in the postscript.)

## Some python package
requests==2.25.1&emsp;
Scrapy==2.4.1&emsp;
selenium==3.141.0&emsp;

## Postscript
Do not use selenium to open an image url.&emsp;
Scrapy will get a response of html about processing image so that ImagePipeline can not handle this kind of response.&emsp;
So be cautious.