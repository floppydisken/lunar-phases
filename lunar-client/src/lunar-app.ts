import { css, html, LitElement } from "lit";
import { customElement } from "lit/decorators";
import { Api } from "./api";

export type LunarPhaseResult = {
  phase: string;
  illuminationPct: number;
  phasePct: number;
};

@customElement("lunar-app")
export class LunarApp extends LitElement {
  static style = css`
    .page {
      display: grid;
      place-items: center;
    }
  `;

  private api: Api;
  private isAuthenticated: boolean = false;

  private result?: LunarPhaseResult;

  constructor() {
    super();

    this.api = new Api();
  }

  login() {}

  render() {
    return html`${this.isAuthenticated
      ? html`<div class="page">
          ${this.result
            ? html`
                <h1>Phase: ${this.result.phase}</h1>
                <h1>Illuminated: ${this.result.illuminationPct * 100}%</h1>
                <h1>Phase %: ${this.result.phasePct * 100}%</h1>
              `
            : ``}
        </div>`
      : html`<div class="page">
          <div>
            <form>
              <input id="username" type="text" />
              <input id="password" type="password" />
              <button @click=${this.login}>Login</button>
            </form>
          </div>
        </div>`}`;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    "lunar-app": LunarApp;
  }
}
