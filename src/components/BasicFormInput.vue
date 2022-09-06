<template>
    <section :class="disabled === true ? 'disabled' : ''">
        <label>{{ title }}</label>
        <input
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target?.value)"
            :placeholder="placeholder"
            :disabled="disabled === true"
            type="text" />
    </section>
</template>

<script lang="ts">
export default {
    props: ['title', 'placeholder', 'disabled', 'modelValue']
}
</script>

<style lang="scss" scoped>
section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    width: 100%;
    margin-bottom: 40px;

    label {
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 20px;
    }

    input {
        width: 100%;
        font-size: 1.1rem;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgb(0, 0, 0, 0.5);
    }

    input::placeholder {
        opacity: 0.35;
    }
}

section.disabled {
    opacity: 0.25;
}
</style>