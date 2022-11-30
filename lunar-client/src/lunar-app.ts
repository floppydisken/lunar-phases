import { css, html, LitElement } from "lit";
import { customElement } from "lit/decorators.js";
import { Api, LunarPhaseResult } from "./api";

@customElement("lunar-app")
export class LunarApp extends LitElement {
  static style = css`
    .page {
      min-width: 100vw;
      min-height: 100vh;
      display: grid;
      place-items: center;
    }
  `;

  private api: Api;
  private result?: LunarPhaseResult;
  private isAuthenticated: () => boolean = () => !!this.result;

  constructor() {
    super();

    this.api = new Api();
  }

  async login() {
    const username: HTMLInputElement | null =
      this.shadowRoot?.querySelector("#username");
    const password: HTMLInputElement | null =
      this.shadowRoot?.querySelector("#password");

    console.log(username, password);

    if (username && password) {
      this.api.setAuth(username.value, password.value);
      try {
        this.result = await this.api.fetchLunarPhase();
        this.requestUpdate();
      } catch (e) {
        console.warn("Could not fetch lunar phase with error", e);
      }
    }
  }

  render() {
    return html`${this.isAuthenticated()
      ? html`<div class="page">
          ${this.result
            ? html`
                <h1>Phase: ${this.result.phaseName}</h1>
                <h1>Illuminated: ${this.result.illuminationPct * 100}%</h1>
                <h1>Phase %: ${this.result.phasePct * 100}%</h1>
              `
            : ``}
        </div>`
      : html`<div class="page">
          <div>
            <input id="username" type="text" />
            <input id="password" type="password" />
            <button @click="${this.login}">Login</button>
          </div>
        </div>`}`;
  }
}

declare global {
  interface HTMLElementTagNameMap {
    "lunar-app": LunarApp;
  }
}