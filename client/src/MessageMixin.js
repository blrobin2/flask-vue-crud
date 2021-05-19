export default {
  data() {
    return {
      message: undefined,
    };
  },
  methods: {
    setMessage(message, fade = true) {
      this.message = message;
      if (fade) {
        setTimeout(() => {
          this.message = undefined;
        }, 5000);
      }
    },
    setMessageFromError(error) {
      const { message } = error.response.data;
      this.setMessage(message, false);
    },
  },
};
