<template>
  <div class="alert"
    v-bind:class="{'alert-danger': type === 'error', 'alert-success': type === 'ok'}" role="alert">
     {{ message }}
  </div>
</template>

<script>
export default {
  name: 'Alert',
  props: ['message', 'type'],
};
</script>
