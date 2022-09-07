import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import { createStore } from 'vuex';
import App from './App.vue';
import '@/style.scss';

import ResumeFormView from '@/views/ResumeFormView.vue';
import CoverLetterFormView from '@/views/CoverLetterFormView.vue';
import SettingsView from '@/views/SettingsView.vue';

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
        },
        {
            path: '/settings',
            name: 'Settings',
            component: SettingsView
        }
    ]
});

const store = createStore({
    state() {
        return {
            resume: {
                relevantSkills: [],
                competency: 'Microservices'
            },
            coverLetter: {
                nameOfRole: '',
                companyName: '',
                recruiterName: '',
                useCustomRecruiterName: false
            },
            settings: {
                applicantRole: 'Software Engineer',
                coverLetterContent: 'Default'
            }
        }
    },
    mutations: {
        updateSettings(state, payload) {
            state.settings.applicantRole = payload.applicantRole;
            state.settings.coverLetterContent = payload.coverLetterContent;
        }
    }
});

createApp(App)
    .use(router)
    .use(store)
    .mount('#app');
