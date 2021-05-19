<template>
  <div
    class="alert alert-info alert-dismissible fade show"
    role="alert"
    v-show="message"
    ref="messageAlert"
  >
    {{ message }}
    <button type="button" class="btn-close" @click="onClose" aria-label="Close"></button>
  </div>
</template>

<script>
import { Alert } from 'bootstrap';

export default {
  props: ['message'],
  data() {
    return {
      alert: null,
    };
  },
  methods: {
    onClose() {
      this.alert.close();
    },
  },
  mounted() {
    this.alert = new Alert(this.$refs.messageAlert);
  },
  watch: {
    message() {
      if (!this.message) {
        this.alert.close();
      }
    },
  },
};
</script>
