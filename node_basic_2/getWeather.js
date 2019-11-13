const axios = require('axios');

const weather = axios.create({
    baseURL: 'http://api.openweathermap.org/data/2.5/',
    params:{
        APPID:'c4ad7974f3977f8f388a60b5c0267caa'
    }
});

module.exports.getWeather = async function(mode, location, units) {
    return (await weather.get(mode, {
        params:{
            q:location,
            units: units,
        }
    })).data;
};