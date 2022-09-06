import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import '@/style.scss';

import ResumeFormView from '@/views/ResumeFormView.vue';
import CoverLetterFormView from '@/views/CoverLetterFormView.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: to => {
                return {
                    path: '/resume'
                }
            }
        },
        {
            path: '/resume',
            name: 'Resume',
            component: ResumeFormView
        },
        {
            path: '/cv',
            name: 'Cover Letter',
            component: CoverLetterFormView
        }
    ]
});

createApp(App).use(router).mount('#app');
