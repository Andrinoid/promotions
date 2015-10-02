var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');
var watch = require('gulp-watch');
var livereload = require('gulp-livereload');
var postcss = require('gulp-postcss');
var autoprefixer = require('autoprefixer');
var plumber = require('gulp-plumber');
var gutil = require('gulp-util');

var onError = function (err) {
    gutil.beep();
    console.log(err);
};

gulp.task('default', ['build', 'watch'], function() {
  //custom code for default
});

gulp.task('build', ['less']);

gulp.task('watch', function() {
	livereload.listen();
    gulp.watch('static/less/*.less', ['build']);
});

gulp.task('less', function() {
    gulp.src('static/less/*.less')
    	.pipe(plumber({ errorHandler: onError }))
        .pipe(less())
        .pipe(postcss([ autoprefixer({ browsers: ['last 2 versions', 'Explorer 9'] }) ]))
        .pipe(gulp.dest('static/css/'))
        .pipe(livereload());
});


