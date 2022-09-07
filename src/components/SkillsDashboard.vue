<template>
    <section>
        <input type="text" />
        <div className="skillBubbleContainer">
            <SkillBubble
                @remove-skill="(skill) => skills = skills.filter((sk) => sk !== skill)"
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
        skills: []
    }
});
</script>

<style lang="scss" scoped>
section {
    input {
        width: 100%;
        font-size: 1.2rem;
        padding: 15px 20px;
        border: 1px solid rgba(0, 0, 0, 0.5);
        border-radius: 10px;
        margin-bottom: 40px;
    }

    .skillBubbleContainer {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 20px 30px;
        height: 250px;
        margin-bottom: 50px;
    }
}
</style>