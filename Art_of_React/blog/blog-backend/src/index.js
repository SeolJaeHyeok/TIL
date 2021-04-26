// 이 파일에서만 no-global-assgin ESLint 옵션을 비활성화 한다.
// eslint-disable no-global-assign

require = require('esm')(module /*, option */);
module.exports = require('./main.js');
