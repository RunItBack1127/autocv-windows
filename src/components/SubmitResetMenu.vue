<template>
    <footer>
        <input :disabled="disabled === true" type="submit" value="Submit" />
        <input type="button" value="Reset" @click="$emit('resetFormFields')" />
    </footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    methods: {
        onClear() {
            this.$emit("resetFormFields");
        }
    },
    props: {
        disabled: Boolean
    }
})
</script>

<style lang="scss">
footer {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin-bottom: 40px;

    input {
        padding: 30px 80px;
        font-size: 1.2rem;
        border-radius: 10px;
        border: 1px solid #000;
        text-transform: uppercase;
        letter-spacing: 0.25rem;
        cursor: pointer;
    }

    input[type="submit"] {
        background-color: #000;
        color: #fff;
        opacity: 1.0;
        transition: opacity 200ms ease;
    }

    input[type="submit"]:disabled {
        pointer-events: none;
        opacity: 0.25;
    }

    input[type="submit"]:hover {
        opacity: 0.8;
    }

    input[type="button"] {
        background: transparent;
    }

    input:not(:last-child) {
        margin-right: 30px;
    }
}
</style>