const {getWeather} = require('./getWeather');

module.exports.showWeather = function(mode, location, units) {
    getWeather(mode, location, units).then(data => {
        if (mode == 'weather') showDay(data, 
            units == 'imperial' ? 'F°' : 'C°',
            units == 'imperial' ? 'mph' : 'm/s');
    });
};

function showDay(data, tUnit, wUnit) {
    process.stdout.write('\n*******************************************************\n\n');
    process.stdout.write(`Location: ${data.name}\n`);
    process.stdout.write(`Date: ${new Date(data.dt * 1000)}\n`);
    process.stdout.write(`Temperature: ${data.main.temp}${tUnit}\n`);
    process.stdout.write(`Maximum temperature: ${data.main.temp_max}${tUnit} Minimum temperature: ${data.main.temp_min}${tUnit}\n`);
    process.stdout.write(`Wind: ${windDirection(data.wind.deg)} ${data.wind.speed}${wUnit}\n`);
    process.stdout.write('\n*******************************************************\n\n');
}

function windDirection(wind) {
    if (wind > 338 || wind < 22) return 'N';
    if (wind < 67) return 'NE';
    if (wind < 112) return 'E';
    if (wind < 157) return 'SE';
    if (wind < 202) return 'S';
    if (wind < 247) return 'SW';
    if (wind < 292) return 'W';
    return 'NW';
}