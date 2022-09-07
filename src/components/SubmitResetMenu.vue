<template>
    <footer>
        <input type="submit" value="Submit" />
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
    }
})
</script>

<style lang="scss">
footer {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    input {
        padding: 20px 50px;
        font-size: 1.1rem;
        border-radius: 10px;
        border: 1px solid #000;
        text-transform: uppercase;
        letter-spacing: 0.25rem;
        cursor: pointer;
    }

    input[type="submit"] {
        background-color: #000;
        color: #fff;
        opacity: 0.8;
    }

    input[type="submit"]:hover {
        opacity: 1.0;
    }

    input[type="button"] {
        background: transparent;
    }

    input:not(:last-child) {
        margin-right: 30px;
    }
}
</style>