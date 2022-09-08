<template>
    <section>
        <input :disabled="disabled === true" @keypress.self="(e) => processInput(e)" type="text" />
        <div className="skillBubbleContainer">
            <SkillBubble
                :key="skill"
                @modify-skill="(payload: ModifySkillPayload) => $emit('modifySkill', payload)"
                v-for="skill in skills"
                :name="skill" />
        </div>
    </section>
</template>

<script lang="ts">
import SkillBubble from '@/components/SkillBubble.vue';
import { defineComponent } from 'vue';
import type { ModifySkillPayload } from '@/util/ModifySkillPayload';
import { ModifySkillMethod } from '@/util/ModifySkillPayload';

export default defineComponent({
    components: {
        SkillBubble
    },
    props: {
        skills: [],
        disabled: Boolean
    },
    methods: {
        processInput(e: KeyboardEvent) {
            if( e.key === "Enter" ) {
                e.preventDefault();
                if( e.target.value !== "" ) {
                    this.$emit( "modifySkill", {
                        method: ModifySkillMethod.ADD,
                        skill: e.target.value
                    } );
                }
                e.target.value = "";
            }
        }
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

    input:disabled {
        opacity: 0.25;
    }

    .skillBubbleContainer {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 20px 10px;
        height: 250px;
        margin-bottom: 50px;
    }
}
</style>