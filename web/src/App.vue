<template>
  <div id="app" class="container">
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <router-link to="/" class="nav-link">Daily Entry</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/update" class="nav-link">Update Entry</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/report" class="nav-link">Report</router-link>
      </li>
    </ul>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px;
}
</style>
