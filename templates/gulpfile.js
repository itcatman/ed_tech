


let project__folder = "dist";
let source__folder = "src";

let path=
{
    build:
    {
        html: project__folder+"/",
        css: project__folder+"/css/",
        js: project__folder+"/js/",
        img: project__folder+"/images/",
        fonts: project__folder+"/fonts/",
    },
    src:
    {
        html: [source__folder + "/*.html", source__folder + "/blocks/*.html",  "!" + source__folder + "/_*.html"],
        css: [source__folder+"/scss/style.scss", "!" + source__folder + "/*.css"],
        js: source__folder+"/js/*.js",
        img: source__folder+"/images/**/*",
        fonts: source__folder+"/fonts/*.ttf",
    },
    watch:
    {
        html: source__folder+"/**/*.html",
        css: source__folder+"/scss/**/*.scss",
        js: source__folder+"/js/**/*.js",
        img: source__folder+"/images/**/*",
    },
    clean:"./" + project__folder + "./"
}

let { src,dest } = require('gulp');
const gulp                    = require('gulp');
const browsersync             = require("browser-sync").create();
const fileinclude             = require('gulp-file-include');
const del                     = require("del");
const scss                    = require("gulp-sass");
const autoprefixer            = require("gulp-autoprefixer");
const group_media             = require("gulp-group-css-media-queries");
const cleanCSS                = require('gulp-clean-css');
const rename                  = require('gulp-rename');
const uglify                  = require('gulp-uglify-es').default;
const babel                   = require('gulp-babel');
const imagemin                = require('gulp-imagemin');





function browserSync(params)
{
    browsersync.init({
        server:
        {
            baseDir: "./" + project__folder + "/"
        },
        port: 3002,
        notify: false
    })
}

function html()
{
    return src(path.src.html)
        .pipe(fileinclude()) // Собирает файлы в один
        .pipe(dest(path.build.html)) // Обрабатывает событие
        .pipe(browsersync.stream()) // Автоматическая перезагрузка 
}



function css()
{
    return src(path.src.css)

        
        .pipe
        (
            scss
            ({
                outputStyle: "expanded"
            })
        )
        .pipe
        (
            autoprefixer
            ({
                overrideBrowserlist: ["last 5 versions"],
                cascade: true
            })
        )
        .pipe(dest(path.build.css)) // Обрабатывает событие
        .pipe(cleanCSS()) // Сжатие файла для оптимизации для CSS
        .pipe // Создает сжатый файл
        (
            rename
            ({
                extname: ".min.css"
            })
        )
        .pipe(group_media())
        .pipe(dest(path.build.css))
        .pipe(browsersync.stream()) // Автоматическая перезагрузка 
}

function js()
{
    return src(path.src.js)

        .pipe(fileinclude()) // Собирает файлы в один
        .pipe(babel())  // Потдержка старых браузеров
        .pipe(dest(path.build.js)) // Обрабатывает событие
        .pipe(uglify()) // Сжатие файла для оптимизации для JS
        .pipe // Создает сжатый файл
        (
            rename
            ({
                extname: ".min.js"
            })
        )
        
        .pipe(dest(path.build.js)) 
        .pipe(browsersync.stream()) // Автоматическая перезагрузка 
}

function img()
{
    return src(path.src.img)

        .pipe(dest(path.build.img))
        .pipe(src(path.src.img))
        .pipe(dest(path.build.img)) // Обрабатывает событие
        .pipe
        (
            imagemin
            ({
                progressive: true,
                svgoPlugins: [{removeViewBox: false}],
                interlaced: true,
                optimizationLevel: 3
            })
        )
        .pipe(dest(path.build.img)) // Обрабатывает событие
        .pipe(browsersync.stream()) // Автоматическая перезагрузка 
}



function clean()
{
    return del(path.clean);
}


function watchFiles() //Подключение всех функций
{
    gulp.watch([path.watch.html],html);
    
    gulp.watch([path.watch.css],css);
    gulp.watch([path.watch.js],js);
    gulp.watch([path.watch.img],img);
}




let build = gulp.series(clean, gulp.parallel(js,css,html,img));
let watch = gulp.parallel(build,watchFiles,browserSync);

exports.img = img;
exports.js = js;
exports.css = css;
exports.html = html;
exports.build = build;
exports.watch = watch;
exports.default = watch;
