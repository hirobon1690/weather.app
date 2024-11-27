<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer" app>
      <v-list :items="items"></v-list>
      <!--  -->
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Weather</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-card width="400px">
        <WeatherIcon></WeatherIcon>
      </v-card>

      <!--  -->
    </v-main>
  </v-app>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import WeatherIcon from './components/WeatherIcon.vue'

export default {
  name: 'App',

  components: {
    HelloWorld,
    WeatherIcon
  },

  data: () => ({
    drawer: null,
    items: [
      {
        title: 'Foo',
        value: 'foo',
      },
      {
        title: 'Bar',
        value: 'bar',
      },
      {
        title: 'Fizz',
        value: 'fizz',
      },
      {
        title: 'Buzz',
        value: 'buzz',
      },
    ]
    //
  }),
}
</script>
