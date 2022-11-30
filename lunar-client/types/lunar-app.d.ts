import { LitElement } from "lit";
export declare class LunarApp extends LitElement {
    static styles: import("lit").CSSResult;
    private api;
    private result?;
    private isAuthenticated;
    constructor();
    login(): Promise<void>;
    render(): import("lit-html").TemplateResult<1>;
}
declare global {
    interface HTMLElementTagNameMap {
        "lunar-app": LunarApp;
    }
}
