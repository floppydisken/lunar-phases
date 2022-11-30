import { LitElement } from "lit";
export type LunarPhaseResult = {
    phase: string;
    illuminationPct: number;
    phasePct: number;
};
export declare class LunarApp extends LitElement {
    static style: import("lit").CSSResult;
    private api;
    private isAuthenticated;
    private result?;
    constructor();
    login(): void;
    render(): import("lit-html").TemplateResult<1>;
}
declare global {
    interface HTMLElementTagNameMap {
        "lunar-app": LunarApp;
    }
}
