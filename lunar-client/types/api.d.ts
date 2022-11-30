export type LunarPhaseResult = {
    phaseName: string;
    illuminationPct: number;
    phasePct: number;
};
export declare class Api {
    base: string;
    token: string;
    authHeader?: any;
    setAuth(email: string, password: string): void;
    fetchLunarPhase(): Promise<LunarPhaseResult>;
}
