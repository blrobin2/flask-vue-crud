<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <alert :message="message" />
        <hr />
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="addBookModal.show()"
        >Add Book</button>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scole="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-show="books.length == 0">
              <td colspan="4">No books! Why don't you add one?</td>
            </tr>
            <tr v-for="book in books" :key="book.id">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    @click="editBook(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="onDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- Add Book Modal -->
    <div
      class="modal fade"
      ref="addBookModal"
      id="addBookModal"
      tabindex="-1"
      aria-labelledby="addBookModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="addBookModalLabel">Add a New Book</h5>
            <button
              type="button"
              class="btn-close"
              @click="addBookModal.hide()"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <form class="w-100">
              <div class="mb-3">
                <label for="addTitle" class="form-label">Title:</label>
                <input
                  type="text"
                  id="addTitle"
                  name="addTitle"
                  v-model="addBookForm.title"
                  required
                  placeholder="Enter Title"
                  class="form-control"
                >
              </div>
              <div class="mb-3">
                <label for="addAuthor" class="form-label">Author:</label>
                <input
                  type="text"
                  id="addAuthor"
                  name="addAuthor"
                  v-model="addBookForm.author"
                  required
                  placeholder="Enter Author"
                  class="form-control"
                >
              </div>
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  id="addRead"
                  v-model="addBookForm.read"
                >
                <label class="form-check-label" for="addRead">Read?</label>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              @click="addBookModal.hide()"
            >Close</button>
            <button type="submit" class="btn btn-primary" @click="onAddBookSubmit">Submit</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Edit Book Modal -->
    <div
      class="modal fade"
      ref="editBookModal"
      id="editBookModal"
      tabindex="-1"
      aria-labelledby="editBookModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editBookModalLabel">Update Book</h5>
            <button
              type="button"
              class="btn-close"
              @click="editBookModal.hide()"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <form class="w-100">
              <div class="mb-3">
                <label for="editTitle" class="form-label">Title:</label>
                <input
                  type="text"
                  id="editTitle"
                  name="editTitle"
                  v-model="editBookForm.title"
                  required
                  placeholder="Enter Title"
                  class="form-control"
                >
              </div>
              <div class="mb-3">
                <label for="editAuthor" class="form-label">Author:</label>
                <input
                  type="text"
                  id="editAuthor"
                  name="editAuthor"
                  v-model="editBookForm.author"
                  required
                  placeholder="Enter Author"
                  class="form-control"
                >
              </div>
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="checkbox"
                  id="editRead"
                  v-model="editBookForm.read"
                >
                <label class="form-check-label" for="editRead">Read?</label>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              @click="editBookModal.hide()"
            >Close</button>
            <button
              type="submit"
              class="btn btn-primary"
              @click="onUpdateBookSubmit"
            >Submit</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Delete Confirm Modal -->
    <div
      class="modal"
      tabindex="-1"
      ref="deleteConfirmModal"
      id="deleteConfirmModal"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Are you sure you wish to delete {{ deletingBook.title }}?</h5>
            <button
              type="button"
              class="btn-close"
              @click="deleteConfirmModal.hide()"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            This cannot be undone!
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              @click="deleteConfirmModal.hide()"
            >Cancel</button>
            <button
              type="submit"
              class="btn btn-danger"
              @click="onDeleteBookConfirm"
            >Remove</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { Modal } from 'bootstrap';

import Alert from './Alert.vue';
import MessageMixin from '../MessageMixin';

export default {
  components: {
    alert: Alert,
  },
  mixins: [
    MessageMixin,
  ],
  data() {
    return {
      booksTable: null,
      addBookModal: null,
      editBookModal: null,
      addBookForm: {
        title: '',
        author: '',
        read: false,
      },
      editBookForm: {
        id: '',
        title: '',
        author: '',
        read: false,
      },
      deletingBook: {
        id: '',
        title: '',
      },
      books: [],
    };
  },
  methods: {
    getBooks() {
      const path = '/books';
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          this.setMessageFromError(error);
        });
    },
    editBook(book) {
      this.editBookForm = book;
      this.editBookModal.show();
    },
    onAddBookSubmit(event) {
      event.preventDefault();
      this.addBookModal.hide();
      const payload = { ...this.addBookForm };
      this.addBook(payload);
      this.initForm();
    },
    onUpdateBookSubmit(event) {
      event.preventDefault();
      this.editBookModal.hide();
      const payload = { ...this.editBookForm };
      this.updateBook(payload, this.editBookForm.id);
      this.initForm();
    },
    onDeleteBook(book) {
      this.deletingBook.id = book.id;
      this.deletingBook.title = book.title;
      this.deleteConfirmModal.show();
    },
    onDeleteBookConfirm() {
      this.deleteConfirmModal.hide();
      this.removeBook(this.deletingBook.id);
      this.initForm();
    },
    addBook(payload) {
      const path = '/books';
      axios.post(path, payload)
        .then((res) => {
          this.setMessage(res.data.message);
        })
        .catch((error) => {
          this.setMessageFromError(error);
        })
        .finally(() => {
          this.getBooks();
        });
    },
    updateBook(payload, bookId) {
      const path = `/books/${bookId}`;
      axios.put(path, payload)
        .then((res) => {
          this.setMessage(res.data.message);
        })
        .catch((error) => {
          this.setMessageFromError(error);
        })
        .finally(() => {
          this.getBooks();
        });
    },
    removeBook(bookId) {
      const path = `/books/${bookId}`;
      axios.delete(path)
        .then((res) => {
          this.setMessage(res.data.message);
        })
        .catch((error) => {
          this.setMessageFromError(error);
        })
        .finally(() => {
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = false;
      this.editBookForm.id = '';
      this.editBookForm.title = '';
      this.editBookForm.author = '';
      this.editBookForm.read = false;
      this.deletingBook.id = '';
      this.deletingBook.title = '';
    },

  },
  mounted() {
    this.addBookModal = new Modal(this.$refs.addBookModal);
    this.editBookModal = new Modal(this.$refs.editBookModal);
    this.deleteConfirmModal = new Modal(this.$refs.deleteConfirmModal);
  },
  created() {
    this.getBooks();
  },
};
</script>
