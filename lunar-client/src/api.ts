export type LunarPhaseResult = {
  phaseName: string;
  illuminationPct: number;
  phasePct: number;
};

export class Api {
  base: string = "http://0.0.0.0:7000/api";
  token: string = "";

  authHeader?: any;

  setAuth(email: string, password: string) {
    const loginPair = btoa(`${email}:${password}`);
    this.authHeader = { Authorization: `Basic ${loginPair}` };
  }

  async fetchLunarPhase() {
    if (!this.authHeader) {
      console.warn("Not authorized to view lunar phase. Please login.");
    }

    const response = await fetch(`${this.base}/lunarphase`, {
      headers: { ...this.authHeader },
    });

    return await response.json() as LunarPhaseResult;
  }
}
