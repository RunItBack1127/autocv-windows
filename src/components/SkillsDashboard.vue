<template>
    <section>
        <input type="text" />
        <div className="skillBubbleContainer">
            <SkillBubble
                v-for="skill in skills"
                :name="skill" />
        </div>
    </section>
</template>

<script lang="ts">
import SkillBubble from '@/components/SkillBubble.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        SkillBubble
    },
    props: {
        skills: Array<String>
    }
});
</script>

<style lang="scss" scoped>
section {
    input {
        width: 100%;
        max-width: 450px;
        font-size: 1.2rem;
        padding: 15px 20px;
        border: 1px solid rgba(0, 0, 0, 0.5);
        border-radius: 10px;
        margin-bottom: 30px;
    }

    .skillBubbleContainer {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 30px;
    }
}
</style>