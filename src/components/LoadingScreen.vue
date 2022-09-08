<template>
    <article v-show="showLoadingScreen">
        <section>
            <div class="lds-dual-ring"></div>
            <h1>Generating {{ routeName }}</h1>
            <h2>Please wait...</h2>
        </section>
    </article>
</template>

<script lang="ts">
import { useRoute } from 'vue-router';
import { useStore } from 'vuex';
import { computed } from '@vue/reactivity';
import { defineComponent } from '@vue/runtime-core';

export default defineComponent({
    data() {
        const store = useStore();

        return {
            routeName: computed(() => useRoute().name),
            showLoadingScreen: computed(() => store.state.showLoadingScreen)
        }
    }
});
</script>

<style lang="scss" scoped>
article {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(255, 255, 255, 0.95);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 99999;

    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        .lds-dual-ring {
            display: inline-block;
            width: 100px;
            height: 100px;
        }

        .lds-dual-ring:after {
            content: " ";
            display: block;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 1px solid #fff;
            border-color: #000 transparent #000 transparent;
            animation: lds-dual-ring 0.5s linear infinite;
        }

        @keyframes lds-dual-ring {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }

        h1 {
            margin-top: 80px;
            font-size: 2rem;
            font-weight: 300;
        }

        h2 {
            margin-top: 5px;
            font-size: 1.5rem;
            font-weight: 100;
        }
    }
}
</style>