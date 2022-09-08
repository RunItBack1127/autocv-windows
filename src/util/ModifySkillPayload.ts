type ModifySkillPayload = {
    method: ModifySkillMethod,
    skill: string
}

enum ModifySkillMethod {
    ADD = "ADD",
    REMOVE = "REMOVE"
}

export type { ModifySkillPayload };
export { ModifySkillMethod };