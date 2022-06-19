const fs = require('fs');
const path = require('path');

module.exports.flag = fs.readFileSync(path.join(__dirname, 'flag.gql'), 'utf8');
module.exports.post = fs.readFileSync(path.join(__dirname, 'post.gql'), 'utf8');
module.exports.posts = fs.readFileSync(path.join(__dirname, 'posts.gql'), 'utf8');
