# 🛰️ SpaceSignal（スペースシグナル）

[한국어](README.md) | [English](README.en.md)

**SpaceSignal**は、世界中の衛星のリアルタイム位置と地上局通信ログを地図上で直感的に探索できるWebサービスです。

> **現在の状態：** Phase 1 開発中（位置ベースの衛星追跡＆デプロイ）

## プロジェクト目標
- **リアルタイム衛星追跡：** ユーザーの現在位置上空を通過する衛星をリアルタイムで計算・可視化します。
- **通信ログ解析：** 世界中の地上局で受信された衛星信号データに基づいて通信状況を監視します。
- **地上局可視化：** 世界中の地上局の観測履歴を地図ベースで提供します。

## はじめに

### 前提条件
- Docker
- Docker Compose

### 実行方法

1. プロジェクトをクローン
```bash
git clone https://github.com/thelight0804/SpaceSignal
cd SpaceSignal
```

2. Docker Composeで全サービスを実行
```bash
docker compose up
```

3. サービスへアクセス
- **Backend API:** http://localhost:8000
- **Frontend:** http://localhost:5173
- **APIドキュメント (Swagger):** http://localhost:8000/docs

### サービスの停止
```bash
docker compose down
```

## 技術スタック

### Backend
- **言語：** Python 3.13+
- **フレームワーク：** FastAPI
- **データベース：** Amazon RDS for PostgreSQL 14+

### Frontend
- **フレームワーク：** Svelte (Vite)

### Infrastructure
- **コンテナ：** Docker & Docker Compose
- **クラウド：** AWS
- **IaC：** Terraform
- **CI/CD：** GitHub Actions

## ロードマップ

### Phase 1: 位置ベースの衛星追跡＆デプロイ（現在）
- [ ] ユーザー位置ベースの衛星位置API開発
- [ ] TLE（軌道データ）データの自動同期
- [ ] Svelteベースの地図UI実装
- [ ] Dockerコンテナ化とdocker-compose構成
- [ ] AWS EC2デプロイとネットワーク設定

### Phase 2: 衛星別通信ログ照会
- [ ] 衛星通信ログデータベース設計
- [ ] 衛星別受信ログ照会API開発
- [ ] 衛星別周波数帯域可視化

### Phase 3: 地上局別通信ログ照会
- [ ] 世界中の地上局位置と観測履歴照会API開発
- [ ] 国家/地域別地上局フィルタリング機能
