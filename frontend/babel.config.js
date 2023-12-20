module.exports = function (api) {
  api.cache(true);
  return {
    presets: ["babel-preset-expo", "module:metro-react-native-babel-preset"],
    plugins: [
      "styled-components",
      "@babel/plugin-transform-flow-strip-types",
      [
        "module-resolver",
        {
          root: ["."],
          alias: {
            assets: "./assets",
          },
        },
      ],
    ],
  };
};
