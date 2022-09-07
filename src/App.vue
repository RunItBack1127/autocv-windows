<template>
    <SiteHeader />
    <main>
        <aside>
            <h1>Choose Category</h1>
            <ul>
                <li :class="routeName === 'Resume' ? 'current-tab' : ''">
                    <router-link to="/resume">Resum&#x00e9</router-link>
                </li>
                <li class="cv-tab" :class="routeName === 'Cover Letter' ? 'current-tab' : ''">
                    <router-link to="/cv">Cover Letter</router-link>
                    <button @click="copyCoverLetter">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-save" viewBox="0 0 16 16">
                            <path d="M2 1a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H9.5a1 1 0 0 0-1 1v7.293l2.646-2.647a.5.5 0 0 1 .708.708l-3.5 3.5a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L7.5 9.293V2a2 2 0 0 1 2-2H14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h2.5a.5.5 0 0 1 0 1H2z"/>
                        </svg>
                    </button>
                </li>
                <li class="settings-tab" :class="routeName === 'Settings' ? 'current-tab' : ''">
                    <router-link to="/settings">Settings</router-link>
                </li>
            </ul>
        </aside>
        <router-view></router-view>
    </main>
    <footer :class="showSuccessCopyDialog === true ? 'show-dialog' : ''" class="copy-dialog success">
        <p>Successfully copied cover letter contents to clipboard.</p>
    </footer>
    <footer :class="showFailCopyDialog === true ? 'show-dialog' : ''" class="copy-dialog fail">
        <p>Error occurred while copying cover letter contents to clipboard.</p>
    </footer>
</template>

<script lang="ts">
import SiteHeader from '@/components/SiteHeader.vue';
import { computed } from '@vue/reactivity';
import { defineComponent } from 'vue';
import { useRoute } from 'vue-router';

export default defineComponent({
    components: {
        SiteHeader
    },
    methods: {
        copyCoverLetter() {
            this.showSuccessCopyDialog = true;
            setTimeout(() => {
                this.showSuccessCopyDialog = false;
            }, 3000);
        }
    },
    data() {
        return {
            routeName: computed(() => useRoute().name),
            showSuccessCopyDialog: false,
            showFailCopyDialog: false
        }
    }
});
</script>

<style lang="scss" scoped>
main {
    display: grid;
    grid-template-columns: 400px 1fr;
    gap: 0 100px;
    width: 80%;
    height: 100%;
    margin: 75px auto 0;
    max-width: 1200px;

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
                    background: transparent;
                    text-align: left;
                    border: none;
                    transition: opacity 150ms ease;
                }

                a.router-link-active {
                    opacity: 1.0;
                }
            }

            li.settings-tab {
                position: relative;
                top: 100px;
            }

            li.cv-tab {

                button {
                    width: 20px;
                    height: 20px;
                    position: relative;
                    margin: auto 0;
                    left: -50px;
                    opacity: 0.0;
                    transition: opacity 150ms ease;
                    pointer-events: none;
                    border: none;
                    background: transparent;
                }
            }

            li.cv-tab.current-tab {

                button {
                    opacity: 1.0;
                    pointer-events: unset;
                    transition: opacity 250ms ease;
                }

                button:hover {
                    opacity: 0.35;
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

footer.copy-dialog {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    margin: 0 auto;
    bottom: 30px;
    width: 100%;
    transition: opacity 1000ms ease-in-out;
    opacity: 0.0;

    p {
        text-align: center;
        font-size: 1rem;
        width: 60%;
        max-width: 800px;
        background-color: rgb(230, 230, 230);
        padding: 30px 0;
        border-radius: 15px;
        color: #000;
    }
}

footer.copy-dialog.show-dialog {
    opacity: 1.0;
}
</style>
