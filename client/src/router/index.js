import { createRouter, createWebHistory } from 'vue-router';

import Book from '../components/Book.vue';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';

const routes = [
  {
    path: '/',
    name: 'Books',
    component: Books,
  }, {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  }, {
    path: '/books/:id',
    name: 'Book',
    component: Book,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
