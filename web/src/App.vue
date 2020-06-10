<template>
  <div id="app" class="container">
    <router-link to="/">Daily Entry</router-link>&nbsp;|
    <router-link to="/report">Report</router-link>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px;
}
</style>
