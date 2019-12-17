const fs = require('fs');

if (fs.existsSync('counter.txt')) {
    const content = fs.readFileSync('counter.txt');
    if (content == parseInt(content)) {
        fs.writeFileSync('counter.txt', (+content + 1).toString());
        process.exit(0);
    } else {
        process.exit(1);
    }
} else {
    fs.writeFileSync('counter.txt', '1');
    process.exit(0);
}