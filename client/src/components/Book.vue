<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 v-show="book.title"><em>{{ book.title }}</em> by {{ book.author }}</h1>
        <alert :message="message" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import * as validate from 'uuid-validate';

import Alert from './Alert.vue';
import MessageMixin from '../MessageMixin';

export default {
  mixins: [
    MessageMixin,
  ],
  components: {
    alert: Alert,
  },
  data() {
    return {
      book: {
        title: '',
        author: '',
      },
    };
  },
  methods: {
    getBook() {
      const { id } = this.$route.params;
      if (!validate(id, 4)) {
        throw new Error('Invalid UUID');
      }
      const path = `/books/${id}`;
      axios
        .get(path)
        .then((res) => {
          const { book } = res.data;
          this.book.title = book.title;
          this.book.author = book.author;
        })
        .catch((error) => {
          this.setMessageFromError(error);
        });
    },
  },
  created() {
    this.getBook();
  },
};
</script>
