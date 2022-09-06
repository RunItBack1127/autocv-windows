<template>
    <SiteHeader />
    <main>
        <aside>
            <h1>Choose Category</h1>
            <ul>
                <li :class="routeName === 'Resume' ? 'current-tab' : ''">
                    <router-link to="/resume">Resume</router-link>
                </li>
                <li :class="routeName === 'Cover Letter' ? 'current-tab' : ''">
                    <router-link to="/cv">Cover Letter</router-link>
                </li>
            </ul>
        </aside>
        <router-view></router-view>
    </main>
</template>

<script setup lang="ts">
import SiteHeader from '@/components/SiteHeader.vue';
import { computed } from '@vue/reactivity';
import { useRoute } from 'vue-router';

const route = useRoute();
const routeName = computed(() => route.name);
</script>

<style lang="scss" scoped>
main {
    display: grid;
    grid-template-columns: 400px 1fr;
    gap: 0 100px;
    width: 80%;
    height: 100%;
    margin: 100px auto 0;

    aside {
        width: 100%;
        height: 100%;

        h1 {
            font-size: 2rem;
            margin-bottom: 50px;
        }

        ul {

            li {
                width: 100%;
                border-radius: 20px;
                display: flex;
                transform: translateX(-30px);
                transition: background 150ms ease;

                a {
                    width: 100%;
                    padding: 30px 0;
                    font-weight: 300;
                    font-size: 1.25rem;
                    color: #000;
                    opacity: 0.35;
                    padding-left: 30px;
                    transition: opacity 150ms ease;
                }

                a.router-link-active {
                    opacity: 1.0;
                }
            }

            li.current-tab {
                background-color: rgba(200, 200, 200, 0.1);
            }

            li:not(:last-child) {
                margin-bottom: 15px;
            }
        }
    }
}
</style>
