<template>
    <section :class="disabled === true ? 'disabled' : ''">
        <div class="titleContainer">
            <label>{{ title }}</label>
            <p>{{ 'e.g. ' + subText }}</p>
        </div>
        <input
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target?.value)"
            :disabled="disabled === true"
            type="text" />
    </section>
</template>

<script lang="ts">
export default {
    props: ['title', 'subText', 'disabled', 'modelValue']
}
</script>

<style lang="scss" scoped>
section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    width: 100%;
    margin-bottom: 70px;

    .titleContainer {

        label {
            font-size: 2rem;
            font-weight: 700;
        }

        p {
            font-size: 1.25rem;
            font-weight: 300;
            opacity: 0.25;
            margin: 5px 0 20px;
        }
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