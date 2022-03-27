const path = require('path');
const webpack = require('webpack');

module.exports = {
    mode: 'development',
    entry: './src/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    devServer: {
        historyApiFallback: true,
        contentBase: path.resolve(__dirname, './dist'),
        open: true,
        compress: true,
        port: 8080,
    },
    plugins: [
        // ...
        // применять изменения только при горячей перезагрузке
        new webpack.HotModuleReplacementPlugin(),
    ],

    module: {
        rules: [
            {
                test: /\.(scss)$/,

                use: [
                    {
                        // вставить CSS на страницу
                        loader: 'style-loader'
                    },
                    {
                        // переводит CSS в модули CommonJS
                        loader: 'css-loader'
                    },
                    {
                        // Выполнить действия postcss
                        loader: 'postcss-loader',
                        options: {
                            // `postcssOptions` требуется для postcss 8.x;
                            // если Вы используете postcss 7.x пропустите ключ
                            postcssOptions: {
                                // плагины postcss, можно экспортировать в postcss.config.js
                                plugins: function () {
                                    return [
                                        require('autoprefixer')
                                    ];
                                }
                            }
                        }
                    },
                    {
                    // компилирует Sass в CSS
                    loader: 'sass-loader'
                    }
                ]
            }
        ]
    },
    devServer: {
        static: './'
    },
    watch: true,
    watchOptions: {
        aggregateTimeout: 1000,
        // poll: 1000,
        ignored: /node_modules/
    }
};