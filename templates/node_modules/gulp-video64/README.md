# gulp-video64

[<< Forked from gulp-image64 >>](https://github.com/leventekk/gulp-image64)

Convert and replace video-files within your DOM/HTML to base64-encoded data.

## Example

##### gulpfile.js

```js
var gulp = require('gulp');
var video64 = require('gulp-video64');

gulp.task('default', function () {
	gulp.src('index.html')
		.pipe(video64())
		.pipe(gulp.dest('path'));
});
```


##### index.html // Before...

```js
<html>
	<head>
	</head>
	<body>
		<video >
			<source src="sample.mp4" >

...
```


##### path/index.html // ...after:

```html
<html>
	<head>
	</head>
	<body>
		<video >
			<source src="data:video/mp4;base64,..." >

...
```

