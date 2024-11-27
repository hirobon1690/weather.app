<template>
    <h1>横浜市の天気</h1>
    <h1>{{ weather }}</h1>
    <h1>{{ temp[0] }}/{{temp[1]}}</h1>
    <v-btn @click="getWeather">更新</v-btn>
</template>
<script>
import axios from 'axios'
export default {
    name: 'WeatherIcon',
    data: () => ({
        weather: "",
        weatherJson: {},
        temp:[null,null],
    }),
    computed: {
        getWeather() {
            axios.get("https://weather.tsukumijima.net/api/forecast/city/140010")
                .then(response => {
                    console.log("hi")
                    this.weather = response.data.forecasts[0].telop
                    this.temp[0]=response.data.forecasts[0].temperature.min.celsius
                    this.temp[1]=response.data.forecasts[0].temperature.max.celsius
                }
            )
        }
    }
}
</script>