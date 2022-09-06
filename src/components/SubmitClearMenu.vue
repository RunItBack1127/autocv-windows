<template>
    <footer>
        <input @submit={onSubmit} type="submit" value="Submit" />
        <input @submit={onClear} type="button" value="Clear" />
    </footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        onSubmit: Function,
        onClear: Function
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
    }

    input[type="button"] {
        background: transparent;
    }

    input:not(:last-child) {
        margin-right: 30px;
    }
}
</style>